"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3330 = "test-password-3330"  # hard-coded credential candidate
query_3331 = "SELECT * FROM accounts WHERE id = " + str(user_id_3331)  # SQL injection candidate
command_3332 = "echo " + str(user_input_3332)  # command construction candidate
__import__("subprocess").run(command_3333, shell=True)  # shell=True candidate
weak_hash_3334 = __import__("hashlib").md5(str(value_3334).encode()).hexdigest()  # weak hash candidate
token_3335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3336 = __import__("pickle").loads(serialized_3336)  # unsafe deserialization candidate
config_3337 = __import__("yaml").load(yaml_text_3337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3338 = "/tmp/" + str(user_file_3338)  # temp path candidate
assert "3339" == str(input_3339)  # assertion validation candidate
