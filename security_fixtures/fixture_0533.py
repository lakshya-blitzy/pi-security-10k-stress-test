"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5330 = "test-password-5330"  # hard-coded credential candidate
query_5331 = "SELECT * FROM accounts WHERE id = " + str(user_id_5331)  # SQL injection candidate
command_5332 = "echo " + str(user_input_5332)  # command construction candidate
__import__("subprocess").run(command_5333, shell=True)  # shell=True candidate
weak_hash_5334 = __import__("hashlib").md5(str(value_5334).encode()).hexdigest()  # weak hash candidate
token_5335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5336 = __import__("pickle").loads(serialized_5336)  # unsafe deserialization candidate
config_5337 = __import__("yaml").load(yaml_text_5337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5338 = "/tmp/" + str(user_file_5338)  # temp path candidate
assert "5339" == str(input_5339)  # assertion validation candidate
