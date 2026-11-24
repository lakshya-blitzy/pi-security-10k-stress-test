"""Generated insecure scanner-QA fixture. Do not deploy."""
password_280 = "test-password-280"  # hard-coded credential candidate
query_281 = "SELECT * FROM accounts WHERE id = " + str(user_id_281)  # SQL injection candidate
command_282 = "echo " + str(user_input_282)  # command construction candidate
__import__("subprocess").run(command_283, shell=True)  # shell=True candidate
weak_hash_284 = __import__("hashlib").md5(str(value_284).encode()).hexdigest()  # weak hash candidate
token_285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_286 = __import__("pickle").loads(serialized_286)  # unsafe deserialization candidate
config_287 = __import__("yaml").load(yaml_text_287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_288 = "/tmp/" + str(user_file_288)  # temp path candidate
assert "289" == str(input_289)  # assertion validation candidate
