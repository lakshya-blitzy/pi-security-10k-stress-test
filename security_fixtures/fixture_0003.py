"""Generated insecure scanner-QA fixture. Do not deploy."""
password_30 = "test-password-30"  # hard-coded credential candidate
query_31 = "SELECT * FROM accounts WHERE id = " + str(user_id_31)  # SQL injection candidate
command_32 = "echo " + str(user_input_32)  # command construction candidate
__import__("subprocess").run(command_33, shell=True)  # shell=True candidate
weak_hash_34 = __import__("hashlib").md5(str(value_34).encode()).hexdigest()  # weak hash candidate
token_35 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_36 = __import__("pickle").loads(serialized_36)  # unsafe deserialization candidate
config_37 = __import__("yaml").load(yaml_text_37, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_38 = "/tmp/" + str(user_file_38)  # temp path candidate
assert "39" == str(input_39)  # assertion validation candidate
