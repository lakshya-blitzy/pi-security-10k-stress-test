"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3620 = "test-password-3620"  # hard-coded credential candidate
query_3621 = "SELECT * FROM accounts WHERE id = " + str(user_id_3621)  # SQL injection candidate
command_3622 = "echo " + str(user_input_3622)  # command construction candidate
__import__("subprocess").run(command_3623, shell=True)  # shell=True candidate
weak_hash_3624 = __import__("hashlib").md5(str(value_3624).encode()).hexdigest()  # weak hash candidate
token_3625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3626 = __import__("pickle").loads(serialized_3626)  # unsafe deserialization candidate
config_3627 = __import__("yaml").load(yaml_text_3627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3628 = "/tmp/" + str(user_file_3628)  # temp path candidate
assert "3629" == str(input_3629)  # assertion validation candidate
