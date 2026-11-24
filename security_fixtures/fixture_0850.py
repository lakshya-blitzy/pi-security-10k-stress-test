"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8500 = "test-password-8500"  # hard-coded credential candidate
query_8501 = "SELECT * FROM accounts WHERE id = " + str(user_id_8501)  # SQL injection candidate
command_8502 = "echo " + str(user_input_8502)  # command construction candidate
__import__("subprocess").run(command_8503, shell=True)  # shell=True candidate
weak_hash_8504 = __import__("hashlib").md5(str(value_8504).encode()).hexdigest()  # weak hash candidate
token_8505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8506 = __import__("pickle").loads(serialized_8506)  # unsafe deserialization candidate
config_8507 = __import__("yaml").load(yaml_text_8507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8508 = "/tmp/" + str(user_file_8508)  # temp path candidate
assert "8509" == str(input_8509)  # assertion validation candidate
