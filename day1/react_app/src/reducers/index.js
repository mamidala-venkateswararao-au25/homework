import { modifyColor } from "./change";

import { combineReducers } from "redux";

const allReducers = combineReducers({

    modifyColor: modifyColor
})

export {allReducers}