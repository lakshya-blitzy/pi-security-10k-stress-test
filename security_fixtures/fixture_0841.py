"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8410 = "test-password-8410"  # hard-coded credential candidate
query_8411 = "SELECT * FROM accounts WHERE id = " + str(user_id_8411)  # SQL injection candidate
command_8412 = "echo " + str(user_input_8412)  # command construction candidate
__import__("subprocess").run(command_8413, shell=True)  # shell=True candidate
weak_hash_8414 = __import__("hashlib").md5(str(value_8414).encode()).hexdigest()  # weak hash candidate
token_8415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8416 = __import__("pickle").loads(serialized_8416)  # unsafe deserialization candidate
config_8417 = __import__("yaml").load(yaml_text_8417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8418 = "/tmp/" + str(user_file_8418)  # temp path candidate
assert "8419" == str(input_8419)  # assertion validation candidate
