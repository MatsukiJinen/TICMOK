import {v4} from 'uuid';

const DEFAULT_DATA = {
        numbers: 1,
        tableData: [],
        uuid: v4()
}

export const loadStorage = (vue) => {
      const dataString = vue.$storage.get('data')
      const data = (dataString) ? JSON.parse(dataString) : {
        numbers: 1,
        tableData: [],
        uuid: undefined,
        access_token: undefined
	}
	return data
}

export const storeStorage = (vue, key, value) => {

      const dataString = vue.$storage.get('data')
      const data = (dataString) ? JSON.parse(dataString) : DEFAULT_DATA

      vue.$storage.set('data', JSON.stringify({
			...data,
			[key]: value
      }))
}
