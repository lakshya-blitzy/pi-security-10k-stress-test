"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7330 = "test-password-7330"  # hard-coded credential candidate
query_7331 = "SELECT * FROM accounts WHERE id = " + str(user_id_7331)  # SQL injection candidate
command_7332 = "echo " + str(user_input_7332)  # command construction candidate
__import__("subprocess").run(command_7333, shell=True)  # shell=True candidate
weak_hash_7334 = __import__("hashlib").md5(str(value_7334).encode()).hexdigest()  # weak hash candidate
token_7335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7336 = __import__("pickle").loads(serialized_7336)  # unsafe deserialization candidate
config_7337 = __import__("yaml").load(yaml_text_7337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7338 = "/tmp/" + str(user_file_7338)  # temp path candidate
assert "7339" == str(input_7339)  # assertion validation candidate
