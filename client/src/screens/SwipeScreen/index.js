import React, { Component } from 'react';
import { View, Text, Dimensions, Image } from 'react-native';
import CardStack, { Card } from 'react-native-card-stack-swiper';
import { StyleSheet } from 'react-native';
import { styles } from '../SettingsScreen/index'


export default class SwipeScreen extends Component {

    dummyFetch = () => {
      return [
              { name: "Ed",
                userId: 1,
                age: 26,
                image: "//",
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              },
              { name: "Dion",
                userId: 2,
                age: 25,
                image: "//",
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              },
              { name: "Harry",
                userId: 3,
                age: 25,
                image: "//",
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              },
              { name: "Jimmy",
                userId: 4,
                age: 19,
                image: "//",
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              },
              { name: "Astrid",
                userId: 5,
                age: 31,
                image: "//",
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              }
            ];
    }

    onLeftSwipe = () => {
      this.onSwipe("left");
    }

    onRightSwipe = () => {
      this.onSwipe("right");
    }

    onSwipe = (direction) => {
      // check if match
      // else update backend with right swipe
    }

    renderEmpty = () => {
      return(
        <Text>
          No more cards :(((
        </Text>
      );
    }

    render() {
        return (
            <View>
                <CardStack loop={true}
                           verticalSwipe={false}
                           style={cardStyle}
                           renderNoMoreCards={this.renderEmpty}
                           ref={swiper => { this.swiper = swiper }}>
                   {this.dummyFetch().map((item, index) => (
                     <Card
                          style={cardStyle}
                          key={index}
                          onSwipedLeft={this.onLeftSwipe}
                          onSwipedRight={this.onRightSwipe}>
                        <Image style={imageStyle} source={require('./dog.jpg')} />

                        <Text style={styles.title}> {item.name}, {item.age} </Text>
                        <Text style={bioStyle}> {item.bio} </Text>
                        <Text style={bioStyle}> Favourite foods </Text>
                     </Card>
                   ))}
                </CardStack>
            </View>
        );
    }
}

const imageStyle = [
  {
    maxWidth: 325,
    maxHeight: 325,
    overflow: 'hidden'
  }
]

const bioStyle = [
  {
    marginLeft: 10,
    paddingLeft: 10
  }
]

const cardStyle = [
  {
    width: 325,
    height: 600,
    borderColor: 'black',
    borderWidth: 3,
    marginLeft: 20,
    marginTop: 20,
    borderRadius: 10,
    backgroundColor: 'white'
  }
]
