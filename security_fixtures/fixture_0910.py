"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9100 = "test-password-9100"  # hard-coded credential candidate
query_9101 = "SELECT * FROM accounts WHERE id = " + str(user_id_9101)  # SQL injection candidate
command_9102 = "echo " + str(user_input_9102)  # command construction candidate
__import__("subprocess").run(command_9103, shell=True)  # shell=True candidate
weak_hash_9104 = __import__("hashlib").md5(str(value_9104).encode()).hexdigest()  # weak hash candidate
token_9105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9106 = __import__("pickle").loads(serialized_9106)  # unsafe deserialization candidate
config_9107 = __import__("yaml").load(yaml_text_9107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9108 = "/tmp/" + str(user_file_9108)  # temp path candidate
assert "9109" == str(input_9109)  # assertion validation candidate
