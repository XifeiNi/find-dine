// @flow

import React, { Component, Fragment } from "react";
import { StatusBar, FlatList, Animated, View } from "react-native";

import { withNavigation } from "react-navigation";
import styled from "styled-components";

import FloatinActionButton from "../../common/FloatingActionButton"; //~/components/common/FloatingActionButto
import { Alert, TYPES } from "../../common/alert";
import Loading from "../../common/Loading";

import AboutRestaurant from "./components/AboutRestaurant";
import Header from "./components/Header";

import CONSTANTS from "../../../utils/CONSTANTS";

import ResturantsData from "../../../store/ducks/resturants.json";

const Container = styled(View)`
  flex: 1;
`;

const FloatingActionButtonWrapper = styled(View)`
  width: 100%;
  align-items: flex-end;
  position: absolute;
  margin-top: ${({ theme }) => theme.metrics.getHeightFromDP("25%") - 28}px;
  padding-right: ${({ theme }) => theme.metrics.largeSize}px;
`;

type Props = {
  userLocation: Object,
  navigation: Function,
  loading: boolean,
  error: boolean,
  data: Object,
};

type State = {
  indexMenuSelected: number,
};

const AnimatedFlatList = Animated.createAnimatedComponent(FlatList);

class RestaurantDetail extends Component<Props, State> {
  _animatedFlatlistPosition = new Animated.Value(0);
  _animatedFlatlistOpacity = new Animated.Value(1);
  _dishesListRef = null;
  _dishesListWidth = 0;

  state = {
    indexMenuSelected: 0,
  };

  onChangeMenuIndex = (indexSelected: number): void => {
    const { indexMenuSelected } = this.state;

    if (indexMenuSelected === indexSelected) {
      return;
    }

    const animationAppearCombo = Animated.sequence([
      Animated.timing(this._animatedFlatlistPosition, {
        toValue: this._dishesListWidth,
        duration: 150,
        useNativeDriver: true,
      }),

      Animated.timing(this._animatedFlatlistOpacity, {
        toValue: 1,
        duration: 150,
        useNativeDriver: true,
      }),

      Animated.spring(this._animatedFlatlistPosition, {
        toValue: 0,
        bounciness: 6,
        useNativeDriver: true,
      }),
    ]);

    this.animateDishesListToFirstIndex();

    Animated.timing(this._animatedFlatlistOpacity, {
      toValue: 0,
      duration: 150,
      useNativeDriver: true,
    }).start(() => {
      this.setState(
        {
          indexMenuSelected: indexSelected,
        },
        () => animationAppearCombo.start()
      );
    });
  };

  animateDishesListToFirstIndex = (): void => {
    this._dishesListRef.getNode().scrollToIndex({
      animated: true,
      index: 0,
    });
  };

  renderHeaderSection = (
    imageURL: string,
    thumbnailImageURL: string
  ): Object => (
    <Header thumbnailImageURL={thumbnailImageURL} imageURL={imageURL} />
  );

  renderAboutRestaurantSection = (restaurantInfo: Object) => (
    <AboutRestaurant
      {...restaurantInfo}
      address={restaurantInfo.location.address}
    />
  );

  renderFloatingActionButton = (restaurant: Object, userLocation: Object) => {
    const { distance, location, isOpen, name } = restaurant;

    const { navigation } = this.props;

    const mapParams = {
      restaurantLocation: {
        id: "restaurant_location",
        latitude: location.coordinates[0],
        longitude: location.coordinates[1],
      },
      userLocation: {
        ...userLocation,
        id: "user_location",
      },
      status: isOpen,
      distance,
    };

    return (
      <FloatingActionButtonWrapper>
        <FloatinActionButton
          action={() =>
            navigation.navigate(CONSTANTS.ROUTE_RESTAURANT_ADDRESS_MAP, {
              [CONSTANTS.NAVIGATION_PARAM_USER_LOCATION]: mapParams,
              [CONSTANTS.NAVIGATION_PARAM_RESTAURANT_NAME]: name,
            })
          }
          name="map-outline"
          color="primaryColor"
        />
      </FloatingActionButtonWrapper>
    );
  };

  render() {
    const loading = false;
    const error = false;
    const data = ResturantsData[Math.floor(Math.random() * 35)];
    const userLocation = { ...CONSTANTS.FORTALEZA_CITY_LOCATION };
    const shouldShowContent = !loading && !error;

    return (
      <Container>
        <StatusBar
          backgroundColor="transparent"
          barStyle={error || loading ? "dark-content" : "light-content"}
          translucent
          animated
        />
        {loading && <Loading />}
        {error && (
          <Alert type={TYPES.ERROR_SERVER_CONNECTION} withExtraTopPadding />
        )}
        {shouldShowContent && (
          <Fragment>
            {this.renderHeaderSection(data.imageURL, data.thumbnailImageURL)}
            {this.renderAboutRestaurantSection(data)}
            {this.renderFloatingActionButton(data, userLocation)}
            {/* {this.renderMenuSection(data.menu)} */}
          </Fragment>
        )}
      </Container>
    );
  }
}

export default withNavigation(RestaurantDetail);
