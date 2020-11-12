import React, {Component, Fragment } from 'react';
import { StatusBar, View, Text } from 'react-native';

import { ThemeProvider } from 'styled-components';
import { Provider } from 'react-redux';

import './src/config/ReactotronConfig';

import ApplicationNavigator from './src/routes';
import AppTheme from './src/styles';
import store from './src/store';

export default class GamesScreen extends Component {  
  render() {
    return (
      <Fragment>
        <StatusBar
          backgroundColor={AppTheme.colors.androidToolbarColor}
          barStyle="light-content"
          translucent
          animated
        />
       <ThemeProvider
          theme={AppTheme}>
           <Provider
            store={store}
          >
           <ApplicationNavigator /> 
          </Provider> 
       </ThemeProvider> 
       
      </Fragment>
    );
  }
}
/*
export default class GamesScreen extends Component {
  render() {
      return (
          <View>
              <Text> GamesScreen </Text>
          </View>
      );
  }
}

 <ThemeProvider
          theme={AppTheme}
        >
          <Provider
            store={store}
          >
            <ApplicationNavigator />
          </Provider>
        </ThemeProvider>
*/