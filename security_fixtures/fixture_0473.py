"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4730 = "test-password-4730"  # hard-coded credential candidate
query_4731 = "SELECT * FROM accounts WHERE id = " + str(user_id_4731)  # SQL injection candidate
command_4732 = "echo " + str(user_input_4732)  # command construction candidate
__import__("subprocess").run(command_4733, shell=True)  # shell=True candidate
weak_hash_4734 = __import__("hashlib").md5(str(value_4734).encode()).hexdigest()  # weak hash candidate
token_4735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4736 = __import__("pickle").loads(serialized_4736)  # unsafe deserialization candidate
config_4737 = __import__("yaml").load(yaml_text_4737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4738 = "/tmp/" + str(user_file_4738)  # temp path candidate
assert "4739" == str(input_4739)  # assertion validation candidate
