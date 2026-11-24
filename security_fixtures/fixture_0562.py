"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5620 = "test-password-5620"  # hard-coded credential candidate
query_5621 = "SELECT * FROM accounts WHERE id = " + str(user_id_5621)  # SQL injection candidate
command_5622 = "echo " + str(user_input_5622)  # command construction candidate
__import__("subprocess").run(command_5623, shell=True)  # shell=True candidate
weak_hash_5624 = __import__("hashlib").md5(str(value_5624).encode()).hexdigest()  # weak hash candidate
token_5625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5626 = __import__("pickle").loads(serialized_5626)  # unsafe deserialization candidate
config_5627 = __import__("yaml").load(yaml_text_5627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5628 = "/tmp/" + str(user_file_5628)  # temp path candidate
assert "5629" == str(input_5629)  # assertion validation candidate
