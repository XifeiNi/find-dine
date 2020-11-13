import React, { Component } from "react";
import { View } from "react-native";
import { Card, Text } from "react-native-paper";

import Avatar from "../Avatar";
import appStyles from "./styles";
import PropTypes from "prop-types";

export default class GroupItem extends Component {
  onPress = () => {
    alert("Unimplemented feature, this page doesn't have backend support yet");
  };
  render() {
    const { item } = this.props;
    return (
      <Card style={appStyles.card} onPress={this.onPress}>
        <View style={appStyles.cardView}>
          <View style={appStyles.nameView}>
            <Avatar large isGroup />
            <Text style={appStyles.nameText}>{item.name}</Text>
            <Text style={appStyles.last}>Active {item.last_active}</Text>
          </View>
          <View style={appStyles.footer}>
            <Text numberOflines={2} style={appStyles.members}>
              {item.members}
            </Text>
          </View>
        </View>
      </Card>
    );
  }
}

GroupItem.propTypes = {
  item: PropTypes.object,
};
