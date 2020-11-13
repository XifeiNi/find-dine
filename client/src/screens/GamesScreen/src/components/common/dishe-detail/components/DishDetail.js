// @flow

import React, { Fragment } from 'react';
import { StatusBar, View } from 'react-native';

import { withNavigation } from 'react-navigation';
import styled from 'styled-components';

import { Alert, TYPES } from '../../alert';
import Loading from '../../Loading';

import Header from './Header';
import Card from './card';

const Container = styled(View)`
  flex: 1;
  background-color: ${({ theme }) => theme.colors.dark};
`;

type Props = {
  navigation: Function,
  dishDetail: Object,
  loading: Object,
  error: Object,
};

const DishDetail = ({
  navigation,
  dishDetail,
  loading,
  error,
}: Props): Object => {
  const shouldShowContent = Object.keys(dishDetail).length > 0 && !loading && !error;

  return (
    <Fragment>
      <StatusBar
        backgroundColor="transparent"
        barStyle={error || loading ? 'dark-content' : 'light-content'}
        translucent
        animated
      />
      {loading && <Loading />}
      {error && (
        <Alert
          type={TYPES.ERROR_SERVER_CONNECTION}
          withExtraTopPadding
        />
      )}
      {shouldShowContent && (
        <Container>
          <Header
            thumbnailImageURL={dishDetail.dish.thumbnailImageURL}
            restaurantId={dishDetail.restaurant.id}
            imageURL={dishDetail.dish.imageURL}
            navigation={navigation}
          />
          <Card
            dishDetail={dishDetail}
          />
        </Container>
      )}
    </Fragment>
  );
};

export default withNavigation(DishDetail);
