// @flow

import React, { Fragment } from 'react';
import {
  TouchableOpacity, Platform, View, Text,
} from 'react-native';

import { withNavigation } from 'react-navigation';
import Icons from 'react-native-vector-icons/MaterialCommunityIcons';
import styled from 'styled-components';

import ReviewStars from '../../../../common/ReviewStars'; 
import CONSTANTS from '../../../../../utils/CONSTANTS';
import appStyles from '../../../../../styles';

const Container = styled(View)`
  width: ${({ theme }) => theme.metrics.getWidthFromDP('82%')}px;
  margin-horizontal: ${({ theme }) => theme.metrics.getWidthFromDP('9%')}px;
  align-self: flex-end;
`;

const Card = styled(View)`
  width: 100%;
  margin-vertical: ${({ theme }) => theme.metrics.smallSize}px;
  padding-vertical: ${({ theme }) => theme.metrics.smallSize}px;
  padding-horizontal: ${({ theme }) => theme.metrics.mediumSize}px;
  background-color: ${({ theme }) => theme.colors.defaultWhite};
  border-radius: 4px;
`;

const TopRowContentWrapper = styled(View)`
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding-top: ${({ theme }) => theme.metrics.smallSize}px;
`;

const BottomRowContentWrapper = styled(View)`
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-top: ${({ theme }) => theme.metrics.extraSmallSize}px;
`;

const DistanceWrapper = styled(View)`
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
`;

const DistanceText = styled(Text)`
  color: ${({ theme }) => theme.colors.darkText}
  font-size: ${({ theme }) => {
    const percentage = Platform.OS === 'ios' ? '4%' : '4.3%';
    return theme.metrics.getWidthFromDP(percentage);
  }}px;
  font-family: Roboto-Regular;
  padding-left: ${({ theme }) => theme.metrics.extraSmallSize}px;
`;

const RestaurantDescriptionText = styled(Text)`
  color: ${({ theme }) => theme.colors.subText};
  font-size: ${({ theme }) => {
    const percentage = Platform.OS === 'ios' ? '4%' : '4.3%';
    return theme.metrics.getWidthFromDP(percentage);
  }}px;
  font-family: Roboto-Regular;
  padding-left: ${({ theme }) => theme.metrics.extraSmallSize}px;
`;

const RestaurantDescriptionWrapper = styled(View)`
  width: 100%;
  margin-vertical: ${({ theme }) => theme.metrics.smallSize}px;
`;

const RestaurantStatus = styled(Text)`
  color: ${({ color }) => color};
  font-size: ${({ theme }) => {
    const percentage = Platform.OS === 'ios' ? '4%' : '4.3%';
    return theme.metrics.getWidthFromDP(percentage);
  }}px;
  font-family: Roboto-Medium;
`;

const Icon = styled(Icons).attrs(({
  color, theme, name, size,
}) => ({
  color: theme.colors[color],
  name,
  size,
}))``;

const renderRestaurantStatus = (isOpen: boolean): Object => {
  const restaurantStatus = {
    open: {
      color: appStyles.colors.green,
      text: 'Open now',
    },
    closed: {
      color: appStyles.colors.red,
      text: 'Closed now',
    },
  };

  const status = isOpen ? 'open' : 'closed';

  return (
    <RestaurantStatus
      color={restaurantStatus[status].color}
    >
      {restaurantStatus[status].text}
    </RestaurantStatus>
  );
};

const renderDistanceContent = (distance: number): Object => (
  <DistanceWrapper>
    <Icon
      color={appStyles.colors.primaryColor}
      name="directions"
      size={22}
    />
    <DistanceText>{`${Math.floor(Math.random() * 51)} km`}</DistanceText>
  </DistanceWrapper>
);

const renderTopRowContent = (stars: number, distance: number): Object => (
  <TopRowContentWrapper>
    <ReviewStars
      textColor="darkText"
      stars={stars}
    />
    {renderDistanceContent(distance)}
  </TopRowContentWrapper>
);

const renderBottomRowContent = (
  navigation: Function,
  isOpen: boolean,
  id: string,
): Object => (
  <BottomRowContentWrapper>
    {renderRestaurantStatus(isOpen)}
    <TouchableOpacity
      onPress={() => navigation.navigate(CONSTANTS.ROUTE_RESTAURANT_DETAIL, {
        [CONSTANTS.NAVIGATION_PARAM_ID]: id,
      })
      }
    >
      <Icon
        color={appStyles.colors.darkText}
        name="arrow-right"
        size={28}
      />
    </TouchableOpacity>
  </BottomRowContentWrapper>
);

type Props = {
  navigation: Function,
  description: string,
  distance: number,
  isOpen: boolean,
  stars: number,
  id: string,
};

const RestaurantItemList = ({
  description,
  navigation,
  distance,
  isOpen,
  stars,
  id,
}: Props): Object => (
  <Container>
    <Card
      style={{
        ...Platform.select({
          ios: {
            elevation: 1,
            shadowOffset: {
              width: 0,
              height: 0,
            },
            shadowRadius: 3,
            shadowOpacity: 0.35,
          },
          android: {
            elevation: 4,
            shadowOffset: {
              width: 1,
              height: -3,
            },
            shadowRadius: 2,
            shadowOpacity: 5.0,
          },
        }),
      }}
    >
      <Fragment>
        {renderTopRowContent(stars, distance)}
        <RestaurantDescriptionWrapper>
          <RestaurantDescriptionText>{description}</RestaurantDescriptionText>
        </RestaurantDescriptionWrapper>
        {renderBottomRowContent(navigation, isOpen, id)}
      </Fragment>
    </Card>
  </Container>
);

export default withNavigation(RestaurantItemList);
