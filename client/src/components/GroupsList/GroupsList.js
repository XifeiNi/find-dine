import React, { Component } from "react";
import { FlatList } from "react-native";
import GroupsItem from "./GroupItem";
import styles from "./styles";

const data = [
  {
    name: "Fireside Chat",
    last_active: "1 day ago",
    members: "Vicky, Alex Jacob, Alice, William + 320",
  },
  {
    name: "Fire Festival",
    last_active: "30 days ago",
    members: "Vicky, Alex, Bob, William + 256",
  },
  {
    name: "Fast Friending",
    last_active: "30 days ago",
    members: "Tom Jacob, Alex Jacob,Thomas Paul + 400",
  },
  {
    name: "Boardgaming Night",
    last_active: "10 days ago",
    members: "Vicky, Alex, Bob, William + 356",
  },
  {
    name: "Birthday Celebration",
    last_active: "5 days ago",
    members: "Tom Alex, Jacob Samuel, Sam, +12",
  },
  {
    name: "College Buddies",
    last_active: "24 days ago",
    members: "Vicky, Alex, Bob, William + 10",
  },
  {
    name: "Movie Night",
    last_active: "1 day ago",
    members: "Tom Kunc, Meow ,Sam  +2",
  },
  {
    name: "Secret Meetup",
    last_active: "28 days ago",
    members: "Tom Kunc,Cecilia Ni, William Smith",
  },
];

export default class GroupsList extends Component {
  renderItem = ({ item }) => {
    return <GroupsItem item={item} />;
  };

  render() {
    return (
      <FlatList
        data={data}
        contentContainerStyle={styles.list}
        renderItem={this.renderItem}
        showsVerticalScrollIndicator={false}
      />
    );
  }
}
