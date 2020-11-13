
import React, { Component } from 'react';
import { View, Text, Button} from 'react-native';
import { styles } from './index';
import AgeRangeField from './AgeRangeField';
import MaxDistanceField from './MaxDistanceField';
import InterestedInField from './InterestedInField';

export default class PreferencesScreen extends Component {
  state = {
    changesMade: false
  }
  saveChanges = () => {
    // do a post
   this.props.navigation.pop();
 };

 changesMade = () => {
   this.setState({
     changesMade: true
   })
 }

  render() {
    return (<View style={preferenceStyle}>
              <Text style={styles.title}> Preferences </Text>
              <InterestedInField changesMade={this.changesMade} />
              <AgeRangeField changesMade={this.changesMade}/>
              <MaxDistanceField changesMade={this.changesMade}/>
              <Button title="Save"
                      onPress={this.saveChanges}
                      disabled={!this.state.changesMade}/>
            </View>
        );
    }
}

const preferenceStyle = [
  {
    marginLeft: 20,
    maxWidth: 500
  }
]
