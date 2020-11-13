import Immutable from 'seamless-immutable';
import fake from './resturants.json'

export const Types = {
  GET_REQUEST: 'home/GET_REQUEST',
  GET_SUCCESS: 'home/GET_SUCCESS',
  GET_FAILURE: 'home/GET_FAILURE',
};

const initialState = Immutable({
  loading: false,
  error: false,
  data: [],
});

export const Creators = {
  getHomeRequest: () => ({
    type: Types.GET_REQUEST,
  }),

  getHomeSuccess: data => ({
    type: Types.GET_SUCCESS,
    payload: { fake },
  }),

  getHomeFailure: () => ({
    type: Types.GET_FAILURE,
    payload: { fake },
  }),
};

const home = (state = initialState, action) => {
  switch (action.type) {
    case Types.GET_REQUEST:
      return {
        ...state,
        data: fake,
        loading: true,
      };

    case Types.GET_SUCCESS:
      return {
        ...state,
        data: fake,
        loading: false,
      };

    case Types.GET_FAILURE:
      return {
        ...state,
        data: fake,
        loading: false,
      };

    default:
      return state;
  }
};

export default home;
