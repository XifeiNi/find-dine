import React, { Component } from 'react';
import { View, Text, Dimensions, Image, Button, Modal } from 'react-native';
import CardStack, { Card } from 'react-native-card-stack-swiper';
import { StyleSheet } from 'react-native';
import { styles } from '../SettingsScreen/index'


export default class SwipeScreen extends Component {
  state = {
    modalVisible: false,
    matchName: "",
    profile: {}
  }

  setModalVisible = (visible) => {
    this.setState({
      modalVisible: visible
    });
  }

  componentDidMount = () => {
    this.setState({
      profiles: this.fetchFilteredProfiles()
    })
  }

    fetchFilteredProfiles = () => {
      return [
              { name: "Anton",
                userId: 1,
                age: 45,
                image: "./anton.png",
                swipeStatus: -1,
                bio: " It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              },
              { name: "Colette",
                userId: 2,
                age: 23,
                image: "./woman.png",
                swipeStatus: 1,
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              },
              { name: "Alfredo",
                userId: 3,
                age: 21,
                image: "./remy.png",
                swipeStatus: 1,
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              },
              { name: "Skinner",
                userId: 4,
                age: 41,
                image: "./angry.png",
                swipeStatus: 0,
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              },
              { name: "Remy",
                userId: 5,
                age: 15,
                image: "./rat.png",
                swipeStatus: 1,
                bio: "Take a look inside the rehearsal room of The Picture of Dorian Gray. It’s exciting to see this unbeatable creative team bring Oscar Wilde’s notorious novel to the stage."
              }
            ];
    }

    onRightSwipe = (index) => {

     const users = this.state.profiles
     const user = users[parseInt(index, 10)]
      if(user.swipeStatus == 1) {
        this.setState({
          matchName: user.name,
          modalVisible: true
        })
     }
    }


    renderEmpty = () => {
      return(
        <View>
          <Text style={[{marginLeft: 30, marginTop: 40, fontSize: 30, fontWeight: 'bold'}]}>
            No more matches. Check back later:)
          </Text>
        </View>
      );
    }

    render() {
      const requireArray = [require('./anton.png'), require('./woman.png'), require('./remy.png'), require('./angry.png'), require('./rat.png')]

        return (
            <View>
                <Modal
                  animationType="slide"
                  transparent={false}
                  visible={this.state.modalVisible}
                >
                  <Text>You just matched with {this.state.matchName}!</Text>
                  <Button title="close"
                          onPress={()=>{this.setModalVisible(false)}}/>
                </Modal>
                <CardStack loop={false}
                           verticalSwipe={false}
                           style={cardStyle}
                           renderNoMoreCards={this.renderEmpty}
                           onSwipedRight={(index) => {this.onRightSwipe(index)}}
                           ref={swiper => { this.swiper = swiper }}>
                   {this.fetchFilteredProfiles().map((item, index) => (
                     <Card
                          style={cardStyle}
                          key={index}
                      >
                        <Image style={imageStyle} source={requireArray[index]} />
                        <Text style={styles.title}> {item.name}, {item.age} </Text>
                        <Text style={bioStyle}> {item.bio} </Text>
                        <View style={[{flexDirection: 'row', justifyContent: 'space-between'}]}>
                          <Button title="Not for me" onPress={() => this.swiper.swipeLeft()}/>
                          <Button title="Bon Appetit" onPress={() => this.swiper.swipeRight()}/>
                        </View>
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
