import React, { Component } from "react";
import { View, TouchableOpacity } from "react-native";
import { SafeAreaView } from "react-navigation";
import { RNCamera } from "react-native-camera";
import Icon from "react-native-vector-icons/MaterialIcons";
import PropTypes from "prop-types";
import MsgStyles from "./styles";

export default class CameraScreen extends Component {
  takePicture = async function() {
    if (this.camera) {
      const options = { quality: 0.5, base64: true };
      const data = await this.camera.takePictureAsync(options);
      alert("Saved", data.uri);
    }
  };

  onPress = () => {
    this.props.navigation.goBack();
  };

  render() {
    return (
      <SafeAreaView style={MsgStyles.container}>
        <RNCamera
          ref={(ref) => {
            this.camera = ref;
          }}
          style={MsgStyles.preview}
          type={RNCamera.Constants.Type.back}
          flashMode={RNCamera.Constants.FlashMode.on}
          permissionDialogTitle={"Permission to use camera"}
          permissionDialogMessage={
            "We need your permission to use your camera phone"
          }
        />
        <SafeAreaView style={MsgStyles.absoluteView}>
          <View style={MsgStyles.head}>
            <TouchableOpacity onPress={this.onPress}>
              <Icon name="close" size={24} color="white" />
            </TouchableOpacity>
          </View>
          <TouchableOpacity
            onPress={this.takePicture.bind(this)}
            style={MsgStyles.capture}
          >
            <Icon name="photo-camera" size={75} color="white" />
          </TouchableOpacity>
        </SafeAreaView>
      </SafeAreaView>
    );
  }
}

CameraScreen.propTypes = {
  navigation: PropTypes.object,
};
