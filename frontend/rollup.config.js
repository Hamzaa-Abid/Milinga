import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { terser } from 'rollup-plugin-terser';
import postcss from 'rollup-plugin-postcss';
import alias from '@rollup/plugin-alias';
import replace from '@rollup/plugin-replace';
import json from '@rollup/plugin-json';

const production = !process.env.ROLLUP_WATCH;

export default {
	input: 'src/main.js',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'app',
		file: '../backend/milinga/static/bundle.js' //'./public/bundle.js'
	},
	plugins: [
		alias({
			resolve: ['.svelte', '.js'], //optional, by default this will just look for .js files or folders
			entries: [
				/*{ find: 'js/websocket.js', replacement: production ? 'src/js/websocketProd.js' : 'src/js/websocketDev.js' }, //websocketDev im Debugging-Modus
				{ find: 'js/ajax.js', replacement: production ? 'src/js/ajaxProd.js' : 'src/js/ajaxDev.js' }, //ajaxDev im Debugging-Modus */
				{ find: '~', replacement: './src' },
				{ find: 'store', replacement: './src/store' },
				{ find: 'ui', replacement: './src/ui' },
				{ find: 'ui_dyn', replacement: './src/ui_dyn' },
				{ find: 'transitions', replacement: './src/ui/transitions' },
				{ find: 'js', replacement: './src/js' },
				{ find: 'svg', replacement: './src/svg' },
			]
		}),

		!production && replace({
			'process.env.NODE_ENV': JSON.stringify('development'),
		}),
		production && replace({
			'process.env.NODE_ENV': JSON.stringify('production'),
		}),

		svelte({
			// enable run-time checks when not in production
			dev: !production,
			// we'll extract any component CSS out into
			// a separate file - better for performance
			css: css => {
				css.write('../backend/milinga/static/bundle.css');
			}
		}),

		// Added for FullCalendar
		postcss(),

		// If you have external dependencies installed from
		// npm, you'll most likely need these plugins. In
		// some cases you'll need additional configuration -
		// consult the documentation for details:
		// https://github.com/rollup/plugins/tree/master/packages/commonjs
		resolve({
			browser: true,
			dedupe: ['svelte']
		}),
		commonjs(),

		// In dev mode, call `npm run start` once
		// the bundle has been generated
		!production && serve(),

		// If we're building for production (npm run build
		// instead of npm run dev), minify
		production && terser(),

		json(),
	],
	watch: {
		clearScreen: false
	}
};

function serve() {
	let started = false;

	return {
		writeBundle() {
			if (!started) {
				started = true;

				require('child_process').spawn('npm', ['run', 'start', '--', '--dev'], {
					stdio: ['ignore', 'inherit', 'inherit'],
					shell: true
				});
			}
		}
	};
}
