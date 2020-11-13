
import React, { Component } from 'react';
import { View, Text, Button} from 'react-native';
import { styles } from './index';
import AgeRangeField from './AgeRangeField';
import MaxDistanceField from './MaxDistanceField';
import InterestedInField from './InterestedInField';

export default class PreferencesScreen extends Component {

  state = {
    changesMade: false,
    errorMessage: "",
    initialFetchError: "",
    initialState: {},
    isLoading: false,
    maxDistance: "",
    mainContentLoaded: false
  }

  saveChanges = () => {
    this.setState({
      isLoading: true,
      changesMade: false
    })
    this.mockPost();
    // this.props.navigation.pop();
  }

  onChangeMaxDistance = (value) => {
    this.setState({
      changesMade: true,
      maxDistance: value
    })
  }

  onChangeInterested = (value) => {
    this.setState({
      changesMade: true,
      interestedIn: value
    })
  }

  onMinChange = (min) => {

    if (min > this.state.maxAge) {
      this.setState({
        maxAge: min
      })
    }

    this.setState({
      changesMade: true,
      minAge: min,
    })

  }

  onMaxChange = (max) => {

    if (max < this.state.minAge) {
      this.setState({
        minAge: max
      })
    }
    this.setState({
      changesMade: true,
      maxAge: max
    })
  }

 // nonmockComponentDidMount = () => {
 //   return fetch('/settingsFetch')
 //    .then((response) => response.json())
 //    .then((json) => {
 //      this.setState({
 //        initialState: json
 //      })
 //    })
 //    .catch((error) => {
 //      this.setState({
 //        initialFetchError: "Something went wrong! Reload the page and try again"
 //      })
 //    })
 //  }

  componentDidMount = () => {
    this.mockFetch()
  //  this.fetchPreferencesAndSet();
  }

  mockFetch = () => {
    this.wait(2000)
    .then((response) => {
      this.setState({
        interestedIn: 'men',
        minAge: 19,
        maxAge: 91,
        maxDistance: 22,
        mainContentLoaded: true
      })
    })
  }
 //
 // fetchprefernces = () => {
 //   this.mockSuccessFetch()
 //    .then((response) => {
 //        this.setState({
 //          initialState: response
 //        })
 //    })
 //    .catch((error) => {
 //      this.setState({
 //        initialFetchError: "Error"
 //      })
 //    });
 // }


 mockPost = () => {
   return this.wait(3000).then((response) => {
     this.props.navigation.pop();
   })
 }

// postPreferences = () => {
//  return fetch('/settingsPost', {
//    method: 'POST',
//    headers: {
//      Accept: 'application/json',
//      'Content-Type': 'application/json'
//    },
//    body: JSON.stringify({
//      interestedIn: this.state.interestedIn,
//      maxAge: this.state.maxAge,
//      minAge: this.state.minAge,
//      maxDistance: this.state.maxDistance
//    })
//  }).then((response) => {
//    this.setState({
//      errorMessage: "",
//      prevInterestedIn: this.state.interestedIn,
//      prevMaxAge: this.state.prevMaxAge,
//      prevMinAge: this.state.prevMinAge,
//      prevMaxDistance: this.state.prevMaxDistance
//    })
//  })
//
// }
//
// mockSuccessFetch = () => {
//   return Promise.resolve(
//     {
//       interestedIn: 'men',
//       minAge: 19,
//       maxAge: 22,
//       maxDistance: 50
//     });
// }


wait = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// mockSuccessfulPost = () => {
//   return Promise.resolve(true)
// }

 // postPreferencesWrapper = () => {
 //   return this.mockSuccessfulPost()
 //   .then((response) => {
 //     this.setState({
 //       isLoading: false
 //     })
 //   })
 //   .catch((error) => {
 //      this.setState({
 //        errorMessage: "Something went wrong :( \n Reload the page and try again",
 //        changesMade: false
 //      })
 //   })
 // }

  render() {
    return ( <>
              { this.state.mainContentLoaded ? <View>
                      <View style={preferenceStyle}>
                        <Text style={styles.title}> Preferences </Text>

                        <InterestedInField value={this.state.interestedIn}
                                           changesMade={this.changesMade}
                                            onChange={this.onChangeInterested} />

                        <AgeRangeField changesMade={this.changesMade}
                                        minAge={this.state.minAge}
                                        maxAge={this.state.maxAge}
                                        onMinChange={this.onMinChange}
                                        onMaxChange={this.onMaxChange}/>

                        <MaxDistanceField changesMade={this.changesMade}
                                          value={this.state.maxDistance}
                                          onChange={this.onChangeMaxDistance}/>

                        <Button title={this.state.isLoading ? "Loading" : "Save"}
                                onPress={this.saveChanges}
                                disabled={!this.state.changesMade}/>

                        <Text> {this.state.errorMessage} </Text>
                      </View>

                </View> : <Text> Preferences Loading</Text>}
                </>
        );
    }
}

const preferenceStyle = [
  {
    marginLeft: 20,
    maxWidth: 500
  }
]
