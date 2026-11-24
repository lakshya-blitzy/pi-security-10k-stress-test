"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6580 = "test-password-6580"  # hard-coded credential candidate
query_6581 = "SELECT * FROM accounts WHERE id = " + str(user_id_6581)  # SQL injection candidate
command_6582 = "echo " + str(user_input_6582)  # command construction candidate
__import__("subprocess").run(command_6583, shell=True)  # shell=True candidate
weak_hash_6584 = __import__("hashlib").md5(str(value_6584).encode()).hexdigest()  # weak hash candidate
token_6585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6586 = __import__("pickle").loads(serialized_6586)  # unsafe deserialization candidate
config_6587 = __import__("yaml").load(yaml_text_6587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6588 = "/tmp/" + str(user_file_6588)  # temp path candidate
assert "6589" == str(input_6589)  # assertion validation candidate
