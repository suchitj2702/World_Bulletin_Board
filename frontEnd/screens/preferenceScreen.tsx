import { StackScreenProps } from '@react-navigation/stack';
import React, { useState, Component } from 'react';
import { StyleSheet, Text, TouchableOpacity, View, ScrollView, Button, TextInput } from 'react-native';
//import * as config from '../config';
import AsyncStorage from '@react-native-async-storage/async-storage';
import MultiSelect from 'react-native-multiple-select';

import { PreferenceParamList, RootStackParamList } from '../types';

export default function PreferenceScreen({ navigation }:

    StackScreenProps<PreferenceParamList, 'PreferenceScreen'>) {
    // Variables that will be used by this tab
    const [selectedItems, setSelectedItems] = useState([]);
    const [getStatus, setStatus] = useState("");

    // store the user's interests into persistant storage
    const storeData = async (value) => {
        try {
            var stringValue = JSON.stringify(value)
            await AsyncStorage.setItem('@storage_Key', stringValue)
            //console.log("Stored: ", stringValue)
        } catch (e) {
            console.log(e)
        }
    }

    //console.log(selectedItems)
    return (
        <ScrollView style={{ flex: 1 }}>
            <MultiSelect
                hideTags
                items={items}
                uniqueKey="id"
                onSelectedItemsChange={sel => setSelectedItems(sel)}
                selectedItems={selectedItems}
                selectText="Pick Items"
                searchInputPlaceholderText="Search Items..."
                onChangeInput={storeData}
                submitButtonText="Update Interests"
                hideSubmitButton={true}
            />
            <Button
                title="Update Interests"
                onPress={() => storeData(selectedItems)}
            />
            <Text>{getStatus}</Text>

        </ScrollView>

    );
}

// a list of possible interests that the user can select from
const items = [
    {
        id: "Adult",
        name: "Adult"
    }, {
        id: "Arts & Entertainment",
        name: "Arts & Entertainment"
    }, {
        id: "Autos & Vehicles",
        name: "Autos & Vehicles"
    }, {
        id: "Beauty & Fitness",
        name: "Beauty & Fitness"
    }, {
        id: "Books & Literature",
        name: "Books & Literature"
    }, {
        id: "Business & Industrial",
        name: "Business & Industrial"
    }, {
        id: "Computers & Electronics",
        name: "Computers & Electronics"
    }, {
        id: "Finance",
        name: "Finance"
    }, {
        id: "Food & Drink",
        name: "Food & Drink"
    }, {
        id: "Games",
        name: "Games"
    }, {
        id: "Health",
        name: "Health"
    }, {
        id: "Hobbies & Leisure",
        name: "Hobbies & Leisure"
    }, {
        id: "Home & Garden",
        name: "Home & Garden"
    }, {
        id: "Internet & Telecom",
        name: "Internet & Telecom"
    }, {
        id: "Jobs & Education",
        name: "Jobs & Education"
    }, {
        id: "Law & Government",
        name: "Law & Government"
    }, {
        id: "News",
        name: "News"
    }, {
        id: "Online Communities",
        name: "Online Communities"
    }, {
        id: "People & Society",
        name: "People & Society"
    }, {
        id: "Pets & Animals",
        name: "Pets & Animals"
    }, {
        id: "Real Estate",
        name: "Real Estate"
    }, {
        id: "Science",
        name: "Science"
    }, {
        id: "Sensitive Subjects",
        name: "Sensitive Subjects"
    }, {
        id: "Shopping",
        name: "Shopping"
    }, {
        id: "Sports",
        name: "Sports"
    }, {
        id: "Travel",
        name: "Travel"
    }
];