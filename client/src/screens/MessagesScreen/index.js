import React, { Component } from "react";
import {
  ScrollView,
  Text,
  TouchableOpacity,
  ImageBackground,
  View,
  FlatList,
} from "react-native";
import { Button } from "react-native-paper";
import PropTypes from "prop-types";
import Message from "./Messages";
import StatusList from "src/components/StatusList";
import demo from "./fake.js";

import styles from "./styles";

export default class MessagesScreen extends Component {
  onPress = () => {
    const { navigation } = this.props;
    navigation.navigate("CameraScreen");
  };

  render() {
    return (
      <View style={styles.container}>
        <StatusList />
        <Button
          icon="add-a-photo"
          mode="contained"
          onPress={() => this.props.navigation.navigate("ChatScreen")}
        >
          Press me
        </Button>
        <FlatList
          data={demo}
          keyExtractor={(item, index) => index.toString()}
          renderItem={({ item }) => (
            <TouchableOpacity
              onPress={() => {
                alert(
                  "This feature is fully functional on backend. Unimplemented on frontend"
                );
                this.props.navigation.navigate("ChatScreen");
              }}
            >
              <Message
                image={item.image}
                name={item.name}
                lastMessage={item.message}
              />
            </TouchableOpacity>
          )}
        />
      </View>
    );
  }
}

MessagesScreen.propTypes = {
  navigation: PropTypes.object,
};
