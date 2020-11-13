import React, { Component } from "react";
import { View } from "react-native";
import { Text } from "react-native-paper";
import PropTypes from "prop-types";

import Avatar from "../Avatar";
import AppStyles from "./styles";
export default class StatusItem extends Component {
  render() {
    const { name, picture } = this.props.item;

    const formattedName = name.first[0].toUpperCase() + name.first.slice(1, 6);
    return (
      <View style={AppStyles.itemView}>
        <Avatar uri={picture.thumbnail} />
        <View style={AppStyles.nameView}>
          <View style={AppStyles.onlineDot} />
          <Text style={AppStyles.nameText}>{formattedName}</Text>
        </View>
      </View>
    );
  }
}

StatusItem.propTypes = {

  item: PropTypes.object,
  name: PropTypes.object,
  picture: PropTypes.object,
};
