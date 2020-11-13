import { createLogger } from "redux-logger";
import { createStore, compose, applyMiddleware } from "redux";
import { persistStore, persistCombineReducers } from "redux-persist";
import createSagaMiddleware from "redux-saga";
import storage from "redux-persist/es/storage"; // default: localStorage if web, AsyncStorage if react-native

import rootReducers from "src/reducers"; // where reducers is a object of reducers
import sagas from "src/sagas";

const config = {
  blacklist: ["loadingReducer"],
  debug: true, 
  key: "root",
  storage,
};

const middleware = [];
const sagaMiddleware = createSagaMiddleware();
middleware.push(sagaMiddleware);

if (__DEV__) {
  middleware.push(createLogger());
}

const reducers = persistCombineReducers(config, rootReducers);

const enhancers = [applyMiddleware(...middleware)];
const persistConfig = { enhancers };
let store = createStore(reducers, undefined, compose(...enhancers));
const persistor = persistStore(store, persistConfig, () => {
});
const configureStore = () => {
  return { persistor, store };
};

sagaMiddleware.run(sagas);

export default configureStore;
