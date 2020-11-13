import React, { Component } from "react";
import { createBottomTabNavigator } from "react-navigation";

import { HomeTabNavigation } from "./HomeTabNavigation";
import CameraScreen from "src/screens/CameraScreen";
import GamesScreen from "src/screens/GamesScreen";
import SettingsApp from "src/screens/SettingsScreen";
import SwipeScreen from "src/screens/SwipeScreen";

import TabIcon from "src/components/TabIcon";
import AppStyles from "src/config/styles";

const HomeTabIcon = ({ tintColor }) => (
  <TabIcon name="chat" tintColor={tintColor} />
);
const PeopleTabIcon = ({ tintColor }) => (
  <TabIcon name="supervisor-account" tintColor={tintColor} />
);
const CameraTabIcon = ({ tintColor }) => (
  <TabIcon name="photo-camera" tintColor={tintColor} type="rounded" />
);
const ResturantTabIcon = ({ tintColor }) => (
  <TabIcon name="bowl" tintColor={tintColor} type="entypo" />
);
const ProfileTabIcon = ({ tintColor }) => (
  <TabIcon name="person" tintColor={tintColor} />
);

export const BottomTabNavigation = createBottomTabNavigator(
  {
    HomeScreen: {
      screen: HomeTabNavigation,
      navigationOptions: {
        header: null,
        tabBarIcon: HomeTabIcon,
      },
    },

    SwipeScreen: {
      screen: SwipeScreen,
      navigationOptions: {
        header: null,
        tabBarIcon: PeopleTabIcon,
      },
    },
    CameraTabScreen: {
      screen: CameraScreen,
      navigationOptions: ({ navigation }) => ({
        header: null,
        tabBarIcon: CameraTabIcon,
        tabBarOnPress: ({ navigation }) => {
          navigation.navigate("CameraScreen");
        },
      }),
    },
    ResturantsScreen: {
      screen: GamesScreen,
      navigationOptions: {
        header: null,
        tabBarIcon: ResturantTabIcon,
      },
    },
    SettingsScreen: {
      screen: SettingsApp,
      navigationOptions: {
        header: null,
        tabBarIcon: ProfileTabIcon,
      },
    },
  },
  {
    tabBarOptions: {
      showLabel: false,
      activeTintColor: "#0084ff",
      inactiveTintColor: AppStyles.colors.inactiveGreyColor,
      pressColor: "#7f8c8d",
    },
  }
);
