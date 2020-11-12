// @flow

import React from 'react';
import { View, Text } from 'react-native';

import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
import styled from 'styled-components';

import { getAlertConfig } from './config';

const Container = styled(View)`
  flex: 1;
  padding-top: ${({ theme, withExtraTopPadding }) => (withExtraTopPadding ? theme.metrics.getHeightFromDP('10%') : 0)}px;
  align-items: center;
`;

const Wrapper = styled(View)`
  justify-content: center;
  align-items: center;
  margin-horizontal: ${({ theme }) => theme.metrics.extraLargeSize}px;
  margin-top: ${({ theme }) => theme.metrics.getHeightFromDP('8%')}px;
`;

const FoodNotFoundIcon = styled(Icon).attrs(({ iconName }) => ({
  name: iconName,
  size: 120,
}))`
  margin-bottom: ${({ theme }) => theme.metrics.extraLargeSize}px;
  color: ${({ theme }) => theme.colors.primaryColor};
`;

const TopText = styled(Text)`
  margin-bottom: ${({ theme }) => theme.metrics.extraLargeSize}px;
  text-align: center;
  color: ${({ theme }) => theme.colors.darkText};
  font-family: Roboto-Light;
  font-size: ${({ theme }) => theme.metrics.getWidthFromDP('8%')}px;
`;

const BottomText = styled(Text)`
  margin-bottom: ${({ theme }) => theme.metrics.extraLargeSize}px;
  color: ${({ theme }) => theme.colors.darkText};
  text-align: center;
  font-family: Roboto-Thin;
  font-size: ${({ theme }) => theme.metrics.getWidthFromDP('5.5%')}px;
`;

const MiddleText = styled(Text)`
  margin-bottom: ${({ theme }) => theme.metrics.extraLargeSize}px;
  color: ${({ theme }) => theme.colors.subText};
  text-align: center;
  font-family: Roboto-Medium;
  font-size: ${({ theme }) => theme.metrics.getWidthFromDP('6%')}px;
`;

type Props = {
  withExtraTopPadding: ?boolean,
  type: string,
};

const Alert = ({ withExtraTopPadding, type }: Props) => {
  const {
    middleText, bottomText, iconName, topText,
  } = getAlertConfig(type);

  return (
    <Container
      withExtraTopPadding={withExtraTopPadding}
    >
      <Wrapper>
        <FoodNotFoundIcon
          iconName={iconName}
        />
        <TopText>{topText}</TopText>
        <MiddleText>{middleText}</MiddleText>
        <BottomText>{bottomText}</BottomText>
      </Wrapper>
    </Container>
  );
};

export default Alert;
