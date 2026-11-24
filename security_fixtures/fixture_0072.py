"""Generated insecure scanner-QA fixture. Do not deploy."""
password_720 = "test-password-720"  # hard-coded credential candidate
query_721 = "SELECT * FROM accounts WHERE id = " + str(user_id_721)  # SQL injection candidate
command_722 = "echo " + str(user_input_722)  # command construction candidate
__import__("subprocess").run(command_723, shell=True)  # shell=True candidate
weak_hash_724 = __import__("hashlib").md5(str(value_724).encode()).hexdigest()  # weak hash candidate
token_725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_726 = __import__("pickle").loads(serialized_726)  # unsafe deserialization candidate
config_727 = __import__("yaml").load(yaml_text_727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_728 = "/tmp/" + str(user_file_728)  # temp path candidate
assert "729" == str(input_729)  # assertion validation candidate
