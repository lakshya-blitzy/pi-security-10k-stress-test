"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8330 = "test-password-8330"  # hard-coded credential candidate
query_8331 = "SELECT * FROM accounts WHERE id = " + str(user_id_8331)  # SQL injection candidate
command_8332 = "echo " + str(user_input_8332)  # command construction candidate
__import__("subprocess").run(command_8333, shell=True)  # shell=True candidate
weak_hash_8334 = __import__("hashlib").md5(str(value_8334).encode()).hexdigest()  # weak hash candidate
token_8335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8336 = __import__("pickle").loads(serialized_8336)  # unsafe deserialization candidate
config_8337 = __import__("yaml").load(yaml_text_8337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8338 = "/tmp/" + str(user_file_8338)  # temp path candidate
assert "8339" == str(input_8339)  # assertion validation candidate
