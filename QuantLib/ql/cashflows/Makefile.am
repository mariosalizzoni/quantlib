
AM_CPPFLAGS = -I${top_srcdir} -I${top_builddir}

this_includedir=${includedir}/${subdir}
this_include_HEADERS = \
    all.hpp \
    averagebmacoupon.hpp \
    capflooredcoupon.hpp \
    capflooredinflationcoupon.hpp \
    cashflows.hpp \
    cashflowvectors.hpp \
    cmscoupon.hpp \
    cmsreplicationpricer.hpp \
    conundrumpricer.hpp \
    coupon.hpp \
    couponpricer.hpp \
    cpicoupon.hpp \
    cpicouponpricer.hpp \
    digitalcmscoupon.hpp \
    digitalcoupon.hpp \
    digitaliborcoupon.hpp \
    dividend.hpp \
    duration.hpp \
    fixedratecoupon.hpp \
    floatingratecoupon.hpp \
    iborcoupon.hpp \
    indexedcashflow.hpp \
    inflationcoupon.hpp \
    inflationcouponpricer.hpp \
    overnightindexedcoupon.hpp \
    rangeaccrual.hpp \
    replication.hpp \
    simplecashflow.hpp \
    timebasket.hpp \
    yoyinflationcoupon.hpp \
    fixedinflationcoupon.hpp \
    zcinflationcapfloor.hpp

libCashFlows_la_SOURCES = \
    averagebmacoupon.cpp \
    capflooredcoupon.cpp \
    capflooredinflationcoupon.cpp \
    cashflows.cpp \
    cashflowvectors.cpp \
    cmscoupon.cpp \
    cmsreplicationpricer.cpp \
    conundrumpricer.cpp \
    coupon.cpp \
    couponpricer.cpp \
    cpicoupon.cpp \
    cpicouponpricer.cpp \
    digitalcmscoupon.cpp \
    digitalcoupon.cpp \
    digitaliborcoupon.cpp \
    dividend.cpp \
    duration.cpp \
    fixedratecoupon.cpp \
    floatingratecoupon.cpp \
    iborcoupon.cpp \
    indexedcashflow.cpp \
    inflationcoupon.cpp \
    inflationcouponpricer.cpp \
    overnightindexedcoupon.cpp \
    rangeaccrual.cpp \
    replication.cpp \
    simplecashflow.cpp \
    timebasket.cpp \
    yoyinflationcoupon.cpp \
    fixedinflationcoupon.cpp \
    zcinflationcapfloor.cpp

noinst_LTLIBRARIES = libCashFlows.la

all.hpp: Makefile.am
	echo "/* This file is automatically generated; do not edit.     */" > $@
	echo "/* Add the files to be included into Makefile.am instead. */" >> $@
	echo >> $@
	for i in $(filter-out all.hpp, $(this_include_HEADERS)); do \
		echo "#include <${subdir}/$$i>" >> $@; \
	done
	echo >> $@
	subdirs='$(SUBDIRS)'; for i in $$subdirs; do \
		echo "#include <${subdir}/$$i/all.hpp>" >> $@; \
	done

