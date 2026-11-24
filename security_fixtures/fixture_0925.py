"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9250 = "test-password-9250"  # hard-coded credential candidate
query_9251 = "SELECT * FROM accounts WHERE id = " + str(user_id_9251)  # SQL injection candidate
command_9252 = "echo " + str(user_input_9252)  # command construction candidate
__import__("subprocess").run(command_9253, shell=True)  # shell=True candidate
weak_hash_9254 = __import__("hashlib").md5(str(value_9254).encode()).hexdigest()  # weak hash candidate
token_9255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9256 = __import__("pickle").loads(serialized_9256)  # unsafe deserialization candidate
config_9257 = __import__("yaml").load(yaml_text_9257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9258 = "/tmp/" + str(user_file_9258)  # temp path candidate
assert "9259" == str(input_9259)  # assertion validation candidate
