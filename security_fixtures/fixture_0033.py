"""Generated insecure scanner-QA fixture. Do not deploy."""
password_330 = "test-password-330"  # hard-coded credential candidate
query_331 = "SELECT * FROM accounts WHERE id = " + str(user_id_331)  # SQL injection candidate
command_332 = "echo " + str(user_input_332)  # command construction candidate
__import__("subprocess").run(command_333, shell=True)  # shell=True candidate
weak_hash_334 = __import__("hashlib").md5(str(value_334).encode()).hexdigest()  # weak hash candidate
token_335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_336 = __import__("pickle").loads(serialized_336)  # unsafe deserialization candidate
config_337 = __import__("yaml").load(yaml_text_337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_338 = "/tmp/" + str(user_file_338)  # temp path candidate
assert "339" == str(input_339)  # assertion validation candidate
