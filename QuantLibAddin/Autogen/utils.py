
"""
 Copyright (C) 2005 Eric Ehlers
 Copyright (C) 2005 Plamen Neykov
 Copyright (C) 2005 Aurelien Chanudet

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it under the
 terms of the QuantLib license.  You should have received a copy of the
 license along with this program; if not, please email quantlib-dev@lists.sf.net
 The license is also available online at http://quantlib.org/html/license.html

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
"""

'utilities'

import common
import time
import sys
import os
import filecmp

# constants

CR_FILENAME = 'stub.copyright'
CR_BUFFER = ''
HEADER = '// this file generated automatically by %s\n\
// editing this file manually is not recommended\n\n'
UPDATE_MSG = '        file %-35s - %s'

def updateIfChanged(fileNew):
    'replace fileOrig with fileNew if they are different'
    fileOrig = fileNew[0:len(fileNew) - len(common.TEMPFILE)]
    if os.path.exists(fileOrig):
        if filecmp.cmp(fileNew, fileOrig):
            os.unlink(fileNew)
            logMessage(UPDATE_MSG % (fileOrig, 'unchanged'))
        else:
            os.unlink(fileOrig)
            os.rename(fileNew, fileOrig)
            logMessage(UPDATE_MSG % (fileOrig, 'updated'))
    else:
        os.rename(fileNew, fileOrig)
        logMessage(UPDATE_MSG % (fileOrig, 'created'))

def printTimeStamp(fileBuf):
    'write autogeneration message to source file'
    fileBuf.write(HEADER % os.path.basename(sys.argv[0]))
    
def printHeader(fileBuf):
    'write copyright and autogeneration message to source file'
    fileBuf.write(common.CR_BUFFER)
    printTimeStamp(fileBuf)

def loadBuffer(fileName):
    'return a buffer containing file fileName'
    fileBuf = open(fileName)
    buffer = fileBuf.read()
    fileBuf.close()
    return buffer

def init():
    'load the copyright stub file to a global buffer'
    common.CR_BUFFER = loadBuffer(CR_FILENAME)

def logMessage(msg):
    'print a message to stdout'
    print time.asctime() + ' ' + msg

def getReturnType(
        returnDef,
        formatAny = '',
        formatScalar = '%s',
        formatVector = 'std::vector < %s >',
        formatMatrix = 'std::vector < std::vector < %s > >',
        replaceLong = '',
        replaceDouble = '',
        replaceBool = '',
        replaceString = '',
        replaceAny = '',
        replaceProperty = '',
        replaceVector = '',
        replaceMatrix = '',
        replaceTensorAny = '',
        prefixScalar = '',
        replacePropertyVector = ''):
    'derive return type for function'

    if returnDef[common.TYPE] == common.PROPERTY \
    and returnDef[common.TENSOR] == common.VECTOR \
    and replacePropertyVector:
            return replacePropertyVector

    if returnDef[common.TENSOR] == common.VECTOR and replaceVector:
        return replaceVector
    elif returnDef[common.TENSOR] == common.MATRIX and replaceMatrix:
        return replaceMatrix
    elif returnDef[common.TYPE] == common.ANY \
    and returnDef[common.TENSOR] != common.SCALAR and replaceTensorAny:
        return replaceTensorAny

    if returnDef[common.TYPE] == common.ANY and formatAny:
        format = formatAny
    elif returnDef[common.TENSOR] == common.SCALAR:
        format = formatScalar
    elif returnDef[common.TENSOR] == common.VECTOR:
        format = formatVector
    elif returnDef[common.TENSOR] == common.MATRIX:
        format = formatMatrix

    if returnDef[common.TYPE] == common.LONG and replaceLong:
        type = replaceLong
    elif returnDef[common.TYPE] == common.DOUBLE and replaceDouble:
        type = replaceDouble
    elif returnDef[common.TYPE] == common.BOOL and replaceBool:
        type = replaceBool
    elif returnDef[common.TYPE] == common.STRING and replaceString:
        type = replaceString
    elif returnDef[common.TYPE] == common.ANY and replaceAny:
        type = replaceAny
    elif returnDef[common.TYPE] == common.PROPERTY and replaceProperty:
        type = replaceProperty
    else:
        type = returnDef[common.TYPE]

    if returnDef[common.TENSOR] == common.SCALAR and prefixScalar \
    and returnDef[common.TYPE] != common.STRING and returnDef[common.TYPE] != common.ANY:
        type = prefixScalar + ' ' + type

    return format % type

def generateConversions(
        paramList, 
        nativeDataType, 
        anyConversion):
    'generate code to convert arrays to vectors/matrices'
    ret = ''
    indent = 8 * ' ';
    bigIndent = 12 * ' ';
    for param in paramList:
        if param[common.TENSOR] == common.SCALAR \
        and param[common.TYPE] != common.ANY:
            continue

        type = param[common.TYPE]
        if param[common.TYPE] == common.LONG:
            suffix = 'Long'
        elif param[common.TYPE] == common.DOUBLE:
            suffix = 'Double'
        elif param[common.TYPE] == common.BOOL:
            suffix = 'Bool'
        elif param[common.TYPE] == common.STRING:
            type = 'std::string'
            suffix = 'String'
        elif param[common.TYPE] == common.ANY:
            type = 'boost::any'
            suffix = 'Any'

        if param[common.TENSOR] == common.SCALAR \
        and param[common.TYPE] == common.ANY: 
            ret += indent + 'boost::any ' + param[common.NAME] + 'Scalar = ' + '\n' \
                + bigIndent + anyConversion + '(' + param[common.NAME] + ');\n'
        elif param[common.TENSOR] == common.VECTOR: 
            ret += indent + 'std::vector < ' + type + ' >' + param[common.NAME] + 'Vector = ' + '\n' \
                + bigIndent + nativeDataType + 'ToVector' + suffix + '(' + param[common.NAME] + ');\n'
        elif param[common.TENSOR] == common.MATRIX: 
            ret += indent + 'std::vector < std::vector < ' + type + ' > >' \
                + param[common.NAME] + 'Matrix = ' + '\n' \
                + bigIndent + nativeDataType + 'ToMatrix' + suffix + '(' + param[common.NAME] + ');\n'

    return ret

def generateFuncCall(function):
    if testAttribute(function, common.CALL_TYPE, 'QL_OBJECT'):
        return 'objectPointer->getObject().' + function[common.QLFUNC]
    else:
        return 'objectPointer->' + function[common.QLFUNC]

def testAttribute(node, attribute, value = ''):
    'test for existence of attribute & for equality to value (if supplied)'
    if not node.has_key(common.ATTS): return False
    if not node[common.ATTS].has_key(attribute): return False
    if value:
         return node[common.ATTS][attribute] == value
    else:
        return True

