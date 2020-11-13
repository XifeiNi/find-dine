import { Platform } from "react-native";
import { createMaterialTopTabNavigator } from "react-navigation";

import MessagesScreen from "src/screens/MessagesScreen";
import ActiveScreen from "src/screens/ActiveScreen";
import GroupsScreen from "src/screens/GroupsScreen";
import CallsScreen from "src/screens/CallsScreen";

import AppStyles from "src/config/styles";

export const HomeTabNavigation = createMaterialTopTabNavigator(
  {
    CallsScreen: {
      screen: CallsScreen,
      navigationOptions: { header: null, title: "Calls" },
    },
    MessagesScreen: {
      screen: MessagesScreen,
      navigationOptions: { header: null, title: "Messages" },
    },

    ActiveScreen: {
      screen: ActiveScreen,
      navigationOptions: { header: null, title: "Active" },
    },
    GroupsScreen: {
      screen: GroupsScreen,
      navigationOptions: { header: null, title: "Groups" },
    },
  },
  {
    tabBarPosition: "top",
    tabBarOptions: {
      activeTintColor: AppStyles.colors.accentColor,
      inactiveTintColor: AppStyles.colors.inactiveGreyColor,
      pressColor: AppStyles.colors.lightGreyCOlor,
      labelStyle: {
        fontFamily: AppStyles.fonts.FONT_MEDIUM,
        fontSize: Platform.OS === "ios" ? 12 : 13,
        fontWeight: "bold",
      },
      indicatorStyle: {
        backgroundColor: AppStyles.colors.accentColor,
      },
      style: {
        backgroundColor: "white",
      },
    },
  }
);
