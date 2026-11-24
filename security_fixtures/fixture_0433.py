"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4330 = "test-password-4330"  # hard-coded credential candidate
query_4331 = "SELECT * FROM accounts WHERE id = " + str(user_id_4331)  # SQL injection candidate
command_4332 = "echo " + str(user_input_4332)  # command construction candidate
__import__("subprocess").run(command_4333, shell=True)  # shell=True candidate
weak_hash_4334 = __import__("hashlib").md5(str(value_4334).encode()).hexdigest()  # weak hash candidate
token_4335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4336 = __import__("pickle").loads(serialized_4336)  # unsafe deserialization candidate
config_4337 = __import__("yaml").load(yaml_text_4337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4338 = "/tmp/" + str(user_file_4338)  # temp path candidate
assert "4339" == str(input_4339)  # assertion validation candidate
