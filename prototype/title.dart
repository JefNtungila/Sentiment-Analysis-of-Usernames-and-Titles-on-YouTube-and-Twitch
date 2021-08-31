import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class FirstScreenTitle extends StatefulWidget {
  @override
  _FirstScreenState createState() {
    return _FirstScreenState();
  }
}

class _FirstScreenState extends State<FirstScreenTitle> {
  // this allows us to access the TextField text
  TextEditingController textFieldController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Sentiment Analyser')),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Padding(
            padding: const EdgeInsets.all(32.0),
            child: TextField(
              controller: textFieldController,
              style: TextStyle(
                fontSize: 24,
                color: Colors.black,
              ),
            ),
          ),
          RaisedButton(
            color: Colors.blue,
            child: Text(
              'analyse sentiment',
              style: TextStyle(fontSize: 24),
            ),
            onPressed: () {
              _sendDataToSecondScreen(context);
              // setState(() {});
            },
          )
        ],
      ),
    );
  }

  // get the text in the TextField and start the Second Screen
  void _sendDataToSecondScreen(BuildContext context) async {
    String textToSend = textFieldController.text;
    String processedString = '';
    await sentimentAnalyser(textToSend).then((String result) {
      setState(() {
        processedString = result;
      });
    });
    Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => SecondScreen(
            processedString: processedString,
          ),
        ));
  }
}

//
class SecondScreen extends StatelessWidget {
  final String processedString;

  // receive data from the FirstScreen as a parameter
  SecondScreen({Key key, @required this.processedString}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text('Sentiment Analyser')),
        body: Center(
            child: Text(processedString, style: TextStyle(fontSize: 24))));
  }
}

Future<String> sentimentAnalyser(sentence) async {
  String url =
      'https://europe-west2-seraphic-camera-313915.cloudfunctions.net/function-3?sentence=$sentence';

  var request = Uri.parse(url);
  var response = await http.post(request, headers: {
    'Access-Control-Allow-Origin': '*', // Required for CORS support to work
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600'
  });
  response.statusCode;

  return response.body;
}
