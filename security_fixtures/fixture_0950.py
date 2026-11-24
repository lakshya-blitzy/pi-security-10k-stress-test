"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9500 = "test-password-9500"  # hard-coded credential candidate
query_9501 = "SELECT * FROM accounts WHERE id = " + str(user_id_9501)  # SQL injection candidate
command_9502 = "echo " + str(user_input_9502)  # command construction candidate
__import__("subprocess").run(command_9503, shell=True)  # shell=True candidate
weak_hash_9504 = __import__("hashlib").md5(str(value_9504).encode()).hexdigest()  # weak hash candidate
token_9505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9506 = __import__("pickle").loads(serialized_9506)  # unsafe deserialization candidate
config_9507 = __import__("yaml").load(yaml_text_9507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9508 = "/tmp/" + str(user_file_9508)  # temp path candidate
assert "9509" == str(input_9509)  # assertion validation candidate
