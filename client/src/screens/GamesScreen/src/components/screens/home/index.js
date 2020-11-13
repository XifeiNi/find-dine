// @flow
import React, { Component } from 'react';
import { View, FlatList } from 'react-native';

import styled from 'styled-components';
import appStyles from '../../../styles';

import RestaurantItemList from './../../screens/near-you/components/restaurants-list/RestaurantItemList';
import ResturantData from '../../../store/ducks/resturants.json';

const ListWrapper = styled(View)`
  flex: 1;
  position: absolute;
`;

type Props = {
  turnOffMoveRestaurantList: Function,
  shouldMoveRestaurantList: boolean,
  indexRestaurantSelected: number,
  restaurants: Array<Object>,
  onSelectMarker: Function,
};

const ITEM_LIST_WIDTH = appStyles.metrics.width;

class RestaurantList extends Component<Props, {}> {
  _restaurantListRef = { };

  componentDidUpdate() {
    const {
      turnOffMoveRestaurantList,
      shouldMoveRestaurantList,
      indexRestaurantSelected,
    } = this.props;

    if (shouldMoveRestaurantList) {
      this.onChangeListIndex(indexRestaurantSelected);
      turnOffMoveRestaurantList();
    }
  }

  onChangeListIndex = (index: number): void => {
    const { restaurants } = this.props;

    if (index >= restaurants.length) {
      return;
    }

    this._restaurantListRef.scrollToIndex({ animated: true, index });
  };

  onSelectMarker = (indexMarkerSelected: number): void => {
    const { indexRestaurantSelected } = this.state;

    if (indexRestaurantSelected === indexMarkerSelected) {
      return;
    }

    /* this.setState({
      indexRestaurantSelected: indexMarkerSelected,
      shouldMoveRestaurantList: true,
    }); */
  };

  onFlatlistMomentumScrollEnd = (event: Object): void => {
    //const { onSelectMarker } = this.props;
    const { contentOffset } = event.nativeEvent;

    const isHorizontalSwipeMovement = contentOffset.x > 0;
    const indexItemSelected = isHorizontalSwipeMovement
      ? Math.ceil(contentOffset.x / appStyles.metrics.width)
      : 0;

    //this.onSelectMarker(indexItemSelected);
  };

  render() {
    const restaurants  = ResturantData;
    console.log(restaurants);

    return (
      <ListWrapper style={{flex: 1}}>
        <FlatList
          //onMomentumScrollEnd={event => this.onFlatlistMomentumScrollEnd(event)}
          renderItem={({ item }) => (
            <RestaurantItemList
              description={item.description}
              distance={item.distance}
              isOpen={item.isOpen}
              stars={item.stars}
              name={item.name}
              id={item.id}
            />
          )}
           /* getItemLayout={(data, index) => ({
            length: ITEM_LIST_LENGTH,
            offset: ITEM_LIST_LENGTH * index,
            index,
          })}  */
          showsVerticalScrollIndicator={true}
          showsHorizontalScrollIndicator={false}
          keyExtractor={item => item["name"]}
          initialNumToRender={50}
          data={restaurants}
          vertical
        />
      </ListWrapper>
    );
  }
}

export default RestaurantList;

/*
import React, { Component } from 'react';
import { ScrollView, RefreshControl, View } from 'react-native';
import styled from 'styled-components';

import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { Creators as HomeCreators } from '../../../store/ducks/home'; // ~/store/ducks/home

import { persistItemInStorage } from '../../../utils/AsyncStoarageManager';
import CONSTANTS from '../../../utils/CONSTANTS';
import appStyles from '../../../styles'; // ~/styles

import { Alert, TYPES } from '../../../components/common/alert';
import Loading from '../../../components/common/Loading'; 

import YouMightLikeSection from './components/you-might-like/home-section';
import InYourCitySection from './components/in-your-city/home-section';
import PopularSection from './components/popular/home-section';

import Section from './components/Section';
import { ROUTE_NAMES } from './routes';

const Container = styled(View)`
  flex: 1;
  background-color: ${({ theme }) => theme.colors.white};
`;

type Props = {
  getHomeRequest: Function,
  homeRequest: Object,
};

type State = {
  isRefresing: boolean,
};

type HomeRequestResult = {
  youMightLikeDishes: Array<Object>,
  inYourCityEvents: Array<Object>,
  popularDishes: Array<Object>,
  userLocation: Object,
};

class Home extends Component<Props, State> {
  state = {
    isRefresing: false,
  };

  componentDidMount() {
    this.requestData();
  }

  async componentWillReceiveProps(nextProps) {
    const { homeRequest } = nextProps;
    const { userLocation } = homeRequest.data;

    if (
      typeof userLocation === 'object'
      && Object.keys(userLocation).length === 2
    ) {
      await persistItemInStorage(
        CONSTANTS.USER_LOCATION,
        JSON.stringify(userLocation),
      );
    }

    this.setState({
      isRefresing: false,
    });
  }

  requestData = (): void => {
    const { getHomeRequest } = this.props;

    getHomeRequest();
  };

  renderMainContent = (data: HomeRequestResult): Object => {
    const { isRefresing } = this.state;

    const { youMightLikeDishes, inYourCityEvents, popularDishes } = data;

    const hasYouMightLikeDishes = youMightLikeDishes && youMightLikeDishes.length > 0;
    const hasInYourCityEvents = inYourCityEvents && inYourCityEvents.length > 0;
    const hasPopularDishes = popularDishes && popularDishes.length > 0;

    return (
      <ScrollView
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl
            progressBackgroundColor={appStyles.colors.primaryColor}
            tintColor={appStyles.colors.primaryColor}
            colors={[appStyles.colors.white]}
            onRefresh={this.requestData}
            refreshing={isRefresing}
          />
        }
      >
        {hasInYourCityEvents && (
          <Section
            nextRoute={ROUTE_NAMES.SEE_ALL_EVENTS}
            title="In Your City"
          >
            <InYourCitySection
              events={inYourCityEvents}
            />
          </Section>
        )}
        {hasYouMightLikeDishes && (
          <Section
            nextRoute={ROUTE_NAMES.YOU_MIGHT_LIKE_SEE_ALL}
            title="You Might Like"
          >
            <YouMightLikeSection
              dishes={youMightLikeDishes}
            />
          </Section>
        )}
        {hasPopularDishes && (
          <Section
            nextRoute={ROUTE_NAMES.POPULAR_SEE_ALL}
            title="Popular"
          >
            <PopularSection
              dishes={popularDishes}
            />
          </Section>
        )}
      </ScrollView>
    );
  };

  render() {
    const { homeRequest } = this.props;
    const { loading, error, data } = homeRequest;

    return (
      <Container>
        {loading && <Loading />}
        {error && <Alert
          type={TYPES.ERROR_SERVER_CONNECTION}
        />}
        {!loading  && this.renderMainContent(data)}
      </Container>
    );
  }
}

const mapStateToProps = state => ({
  homeRequest: state.home,
});

const mapDispatchToProps = dispatch => bindActionCreators(HomeCreators, dispatch);

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Home);
*/