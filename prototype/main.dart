import 'package:flutter/material.dart';
import 'title.dart';
import 'username.dart';

//
void main() {
  runApp(MaterialApp(
      title: 'Sentiment Analyser',
      home: HomeScreen(),
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      )));
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
            appBar: AppBar(title: Text('Sentiment Analyser')),
            body: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                verticalDirection: VerticalDirection.down,
                children: [
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: RaisedButton(
                        onPressed: () {
                          _navigateToUsernameScreen(context);
                        },
                        color: Colors.blue,
                        child: Text(
                          'analyse username',
                          style: TextStyle(fontSize: 24),
                        )),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: RaisedButton(
                        onPressed: () {
                          _navigateToTitleScreen(context);
                        },
                        color: Colors.blue,
                        child: Text(
                          'analyse title',
                          style: TextStyle(fontSize: 24),
                        )),
                  ),
                ],
              ),
            )));
  }

  void _navigateToUsernameScreen(BuildContext context) {
    Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => FirstScreenUsername(),
        ));
  }

  void _navigateToTitleScreen(BuildContext context) {
    Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => FirstScreenTitle(),
        ));
  }
}
