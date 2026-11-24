"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5730 = "test-password-5730"  # hard-coded credential candidate
query_5731 = "SELECT * FROM accounts WHERE id = " + str(user_id_5731)  # SQL injection candidate
command_5732 = "echo " + str(user_input_5732)  # command construction candidate
__import__("subprocess").run(command_5733, shell=True)  # shell=True candidate
weak_hash_5734 = __import__("hashlib").md5(str(value_5734).encode()).hexdigest()  # weak hash candidate
token_5735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5736 = __import__("pickle").loads(serialized_5736)  # unsafe deserialization candidate
config_5737 = __import__("yaml").load(yaml_text_5737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5738 = "/tmp/" + str(user_file_5738)  # temp path candidate
assert "5739" == str(input_5739)  # assertion validation candidate
