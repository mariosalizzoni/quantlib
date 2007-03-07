/* -*- mode: c++; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */

/*
 Copyright (C) 2007 Ferdinando Ametrano
 Copyright (C) 2004 Jeff Yu
 Copyright (C) 2004 M-Dimension Consulting Inc.
 Copyright (C) 2005 StatPro Italia srl

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it
 under the terms of the QuantLib license.  You should have received a
 copy of the license along with this program; if not, please email
 <quantlib-dev@lists.sf.net>. The license is also available online at
 <http://quantlib.org/reference/license.html>.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
*/

/*! \file fixedcouponbond.hpp
    \brief fixed-coupon bond
*/

#ifndef quantlib_fixed_rate_bond_hpp
#define quantlib_fixed_rate_bond_hpp

#include <ql/Instruments/bond.hpp>

namespace QuantLib {

    class Schedule;

    //! fixed-coupon bond
    /*! \ingroup instruments

        \test calculations are tested by checking results against
              cached values.
    */
    class FixedRateBond : public Bond {
      public:
        FixedRateBond(Natural settlementDays,
                      Real faceAmount,
                      const Schedule& schedule,
                      const std::vector<Rate>& coupons,
                      const DayCounter& paymentDayCounter,
                      BusinessDayConvention paymentConvention = Following,
                      Real redemption = 100.0,
                      const Date& issueDate = Date(),
                      const Handle<YieldTermStructure>& discountCurve
                                            = Handle<YieldTermStructure>());
    };

}

#endif
