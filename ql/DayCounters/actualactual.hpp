
/*
 * Copyright (C) 2000-2001 QuantLib Group
 *
 * This file is part of QuantLib.
 * QuantLib is a C++ open source library for financial quantitative
 * analysts and developers --- http://quantlib.org/
 *
 * QuantLib is free software and you are allowed to use, copy, modify, merge,
 * publish, distribute, and/or sell copies of it under the conditions stated
 * in the QuantLib License.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the license for more details.
 *
 * You should have received a copy of the license along with this file;
 * if not, please email quantlib-users@lists.sourceforge.net
 * The license is also available at http://quantlib.org/LICENSE.TXT
 *
 * The members of the QuantLib Group are listed in the Authors.txt file, also
 * available at http://quantlib.org/group.html
*/

/*! \file actualactual.hpp
    \brief act/act day counter

    \fullpath
    ql/DayCounters/%actualactual.hpp
*/

// $Id$

#ifndef quantlib_actualactual_day_counter_h
#define quantlib_actualactual_day_counter_h

#include "ql/daycounter.hpp"

namespace QuantLib {

    namespace DayCounters {

        //! Actual/Actual day count
        /*! The day count can be calculated according to ISMA and US Treasury
            convention, also known as "Actual/Actual (Bond)"; to ISDA, also 
            known as "Actual/Actual (Historical)"; or to AFB, also known as
            "Actual/Actual (Euro)".

            For more details, refer to 
            http://www.isda.org/c_and_a/pdf/mktc1198.pdf
        */
        class ActualActual : public DayCounter {
          public:
            enum Convention { ISMA, Bond, ISDA, Historical, AFB, Euro };
            explicit ActualActual(Convention c = ISMA)
            : convention_(c) {}
            //! \name DayCounter interface
            //@{
            std::string name() const;
            int dayCount(const Date& d1, const Date& d2) const;
            Time yearFraction(const Date& d1, const Date& d2,
                const Date& refPeriodStart, const Date& refPeriodEnd) const;
            //@}
          private:
            Convention convention_;
            Time ismaYearFraction(const Date& d1, const Date& d2,
                const Date& refPeriodStart, const Date& refPeriodEnd) const;
            Time isdaYearFraction(const Date& d1, const Date& d2) const;
            Time afbYearFraction(const Date& d1, const Date& d2) const;
        };

    }

}


#endif
