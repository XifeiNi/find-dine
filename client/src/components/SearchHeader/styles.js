import { StyleSheet } from 'react-native';
import AppStyles from 'src/config/styles';
import { isIphoneX } from 'src/lib/isIphoneX';

const styles = StyleSheet.create({
    search: {
        alignItems: 'center',
        flexDirection: 'row',
        height: 50
    },

    container: {
        backgroundColor: AppStyles.colors.black,
        borderBottomColor: AppStyles.colors.separator,
        borderBottomWidth: StyleSheet.hairlineWidth,
        height: isIphoneX() ? 100 : null,
        justifyContent: 'flex-end'
    },

    searchbar: {
        backgroundColor: AppStyles.colors.white,
        elevation: 0
    },

    elevatedContainer: {
        backgroundColor: AppStyles.colors.black,
        borderBottomColor: AppStyles.colors.separator,
        borderBottomWidth: StyleSheet.hairlineWidth,
        elevation: 4,
        height: isIphoneX() ? 100 : null,
        justifyContent: 'flex-end'
    },

    toolbar: {
        backgroundColor: AppStyles.colors.white
    },

    input: {
        fontFamily: AppStyles.fonts.FONT_REGULAR,
        fontSize: 16,
        height: 40,
        paddingHorizontal: 10,
        width: '90%'
    },

    btn: {
        height: 40,
        justifyContent: 'center',
        paddingHorizontal: 16,
        width: '75%'
    },

    btnText: {
        fontSize: 16,
        fontFamily: AppStyles.fonts.FONT_REGULAR,
        color: '#7f8c8d'
    }
});

export default styles;
