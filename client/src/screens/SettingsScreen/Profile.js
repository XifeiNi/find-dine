import React, { Component, useState} from 'react';
import { View, Text, Button, TextInput, Image, ScrollView } from 'react-native';
import { styles } from './index';
import BioField from './ProfileFields/BioField';
import ImageField from './ProfileFields/ImageField';

export default class ProfileScreen extends Component {

  state = {
    bio: "Hello",
    previousBio: "Hello",
    image: "",
    buttonDisabled: true
  }


  mockFetch = () => {

  }

  mockPost = () => {
    
  }

   saveChanges = () => {
     // postBio();
    this.setState({buttonDisabled: true})
    this.props.navigation.pop();
  };

  updateProfileState = (bio) => {
    this.setState({buttonDisabled: bio == this.state.previousBio})
    if (bio.length <= 200) {
      this.setState({bio: bio});
    }
  }


  render() {
    return (<ScrollView>
              <Text style={styles.title}> Profile </Text>

              <View style={[{maxWidth: 300, marginLeft: 20}]}>
                <Text style={styles.smallText}> Bio </Text>
                <BioField  updateProfileState={this.updateProfileState}
                    value={this.state.bio}
                />
                <Text> {200 - this.state.bio.length} characters left </Text>
                <Text style={styles.smallText}> Display Picture </Text>
                <ImageField />
                <Button title="Save"
                        disabled={this.state.buttonDisabled}
                        onPress={this.saveChanges}
                        style={buttonStyle}
                />
              </View>

          </ScrollView>
        );
    }
}

const buttonStyle = [
  {
    marginTop: 10,
    borderRadius: 10
  }
];
