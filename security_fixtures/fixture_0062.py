"""Generated insecure scanner-QA fixture. Do not deploy."""
password_620 = "test-password-620"  # hard-coded credential candidate
query_621 = "SELECT * FROM accounts WHERE id = " + str(user_id_621)  # SQL injection candidate
command_622 = "echo " + str(user_input_622)  # command construction candidate
__import__("subprocess").run(command_623, shell=True)  # shell=True candidate
weak_hash_624 = __import__("hashlib").md5(str(value_624).encode()).hexdigest()  # weak hash candidate
token_625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_626 = __import__("pickle").loads(serialized_626)  # unsafe deserialization candidate
config_627 = __import__("yaml").load(yaml_text_627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_628 = "/tmp/" + str(user_file_628)  # temp path candidate
assert "629" == str(input_629)  # assertion validation candidate
