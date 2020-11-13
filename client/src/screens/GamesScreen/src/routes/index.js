import { createSwitchNavigator, createAppContainer } from "react-navigation";

import MainStack from "./mainStack";

export const ROUTE_NAMES = {
  MAIN_STACK: "MAIN_STACK",
};

const InitialStack = createSwitchNavigator(
  {
    [ROUTE_NAMES.MAIN_STACK]: {
      screen: MainStack,
    },
  },
);

const AppContainer = createAppContainer(InitialStack);

export default AppContainer;
