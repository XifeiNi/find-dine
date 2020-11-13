import { createSwitchNavigator, createAppContainer } from 'react-navigation';

import MainStack from './mainStack';

export const ROUTE_NAMES = {
  MAIN_STACK: 'MAIN_STACK',
};

const InitialStack = createSwitchNavigator(
  {
    [ROUTE_NAMES.MAIN_STACK]: {
      screen: MainStack,
    },
  },
  {
    initialRouteName: ROUTE_NAMES.ONBOARDING_INTRO,
  },
);

const AppContainer = createAppContainer(InitialStack);

export default AppContainer;
