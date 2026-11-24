"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7620 = "test-password-7620"  # hard-coded credential candidate
query_7621 = "SELECT * FROM accounts WHERE id = " + str(user_id_7621)  # SQL injection candidate
command_7622 = "echo " + str(user_input_7622)  # command construction candidate
__import__("subprocess").run(command_7623, shell=True)  # shell=True candidate
weak_hash_7624 = __import__("hashlib").md5(str(value_7624).encode()).hexdigest()  # weak hash candidate
token_7625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7626 = __import__("pickle").loads(serialized_7626)  # unsafe deserialization candidate
config_7627 = __import__("yaml").load(yaml_text_7627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7628 = "/tmp/" + str(user_file_7628)  # temp path candidate
assert "7629" == str(input_7629)  # assertion validation candidate
